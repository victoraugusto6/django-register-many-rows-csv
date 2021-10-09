from project.file.models import File


def test_send_file(db):
    File.objects.create(
        file='10_mil.csv'
    )

    assert File.objects.exists()
