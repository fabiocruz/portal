import json

import pandas as pd
from django.core.management.base import BaseCommand

from portal.capstone import models


class Command(BaseCommand):
    help = "Load file to datapoints"

    def add_arguments(self, parser):
        parser.add_argument("simulator_name")
        parser.add_argument("--data", required=True)
        parser.add_argument("--outcomes")
        parser.add_argument("--batch-size", type=int, default=1000)

    def handle(self, *args, **options):
        simulator = models.Simulator.objects.get(
            name=options["simulator_name"]
        )
        data = pd.read_csv(options["data"])

        outcome_iter = None
        if options["outcomes"]:
            outcomes = pd.read_csv(options["outcomes"])
            outcome_iter = outcomes.iterrows()

        self.stdout.write(
            self.style.SUCCESS("Creating datapoint objects batch 1")
        )
        datapoints = []
        for idx, obs in data.iterrows():
            data = obs.to_dict()
            id_ = data["id"]
            del data["id"]
            data = {"id": id_, "observation": data}
            dt = models.Datapoint(simulator=simulator, data=json.dumps(data))
            if outcome_iter:
                out = next(outcome_iter)[1].to_dict()
                out["true_class"] = out.pop("ContrabandIndicator")
                dt.outcome = json.dumps(out)
            datapoints.append(dt)

            if (idx + 1) % options["batch_size"] == 0:
                batch_num = (idx // options["batch_size"]) + 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Storing in database batch {batch_num}"
                    )
                )
                models.Datapoint.objects.bulk_create(datapoints)

                self.stdout.write(
                    self.style.SUCCESS(
                        "Creating datapoint objects batch " f"{batch_num + 1}"
                    )
                )
                datapoints = []

        if datapoints:
            batch_num = idx // options["batch_size"]
            self.stdout.write(
                self.style.SUCCESS(f"Storing in database batch {batch_num}")
            )
            models.Datapoint.objects.bulk_create(datapoints)

        self.stdout.write(
            self.style.SUCCESS("Successfully created datapoints")
        )
