from django.urls import path

from portal.candidate import views


app_name = "candidate"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path(
        "code-of-conduct", views.CodeOfConductView.as_view(), name="codeofconduct"
    ),
    path("scholarship", views.ScholarshipView.as_view(), name="scholarship"),
    path(
        "before-coding-test",
        views.candidate_before_coding_test_view,
        name="before-candidate-coding-test",
    ),
    path(
        "coding-test",
        views.candidate_coding_test_view,
        name="candidate-coding-test",
    ),
    path(
        "slu/<slug:submission_type>", views.candidate_slu_view, name="candidate-slu"
    ),
    path(
        "assignment-download",
        views.candidate_assignment_download_view,
        name="candidate-assignment-download",
    ),
    path(
        "submissions/upload/<slug:submission_type>",
        views.candidate_submission_upload_view,
        name="candidate-submissions-upload",
    ),
    path(
        "submission/<slug:submission_type>/<int:submission_id>",
        views.candidate_submission_download_view,
        name="candidate-coding-submission-download",
    ),
    path(
        "submission/feedback/<slug:submission_type>/<int:submission_id>",
        views.candidate_submission_feedback_download_view,
        name="candidate-coding-feedback-download",
    ),
    path("payment", views.candidate_payment_view, name="candidate-payment"),
    path(
        "payment/download-document/<int:document_id>",
        views.candidate_document_download_view,
        name="candidate-payment-document-download",
    ),
    path(
        "payment/upload-payment-proof",
        views.candidate_payment_proof_upload_view,
        name="candidate-payment-proof-upload",
    ),
    path(
        "payment/upload-student-id",
        views.candidate_student_id_upload_view,
        name="candidate-student-id-upload",
    ),
]
