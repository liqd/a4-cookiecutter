import os

import pytest
from django.conf import settings
from django.urls import reverse

from adhocracy4.comments import models as comments_models
from adhocracy4.ratings import models as rating_models
from apps.mapideas import models as mapidea_models
from tests.helpers import createThumbnail


@pytest.mark.django_db
def test_absolute_url(map_idea_factory):
    mapidea = map_idea_factory()
    url = reverse('mapidea-detail',
                  kwargs={'slug': mapidea.slug})
    assert mapidea.get_absolute_url() == url


@pytest.mark.django_db
def test_save(map_idea_factory):
    mapidea = map_idea_factory()
    assert '<script>' not in mapidea.description


@pytest.mark.django_db
def test_str(map_idea_factory):
    mapidea = map_idea_factory()
    mapidea_string = mapidea.__str__()
    assert mapidea_string == mapidea.name


@pytest.mark.django_db
def test_project(map_idea_factory):
    mapidea = map_idea_factory()
    assert mapidea.module.project == mapidea.project


@pytest.mark.django_db
def test_delete_mapidea(map_idea_factory, comment_factory,
                        rating_factory, ImagePNG):
    mapidea = map_idea_factory(image=ImagePNG)
    image_path = os.path.join(settings.MEDIA_ROOT, mapidea.image.path)
    thumbnail_path = createThumbnail(mapidea.image)

    for i in range(5):
        comment_factory(content_object=mapidea)
    comment_count = comments_models.Comment.objects.all().count()
    assert comment_count == len(mapidea.comments.all())

    rating_factory(content_object=mapidea)
    rating_count = rating_models.Rating.objects.all().count()

    assert os.path.isfile(image_path)
    assert os.path.isfile(thumbnail_path)
    count = mapidea_models.MapIdea.objects.all().count()
    assert count == 1
    assert comment_count == 5
    assert rating_count == 1

    mapidea.delete()
    assert not os.path.isfile(image_path)
    assert not os.path.isfile(thumbnail_path)
    count = mapidea_models.MapIdea.objects.all().count()
    comment_count = comments_models.Comment.objects.all().count()
    rating_count = rating_models.Rating.objects.all().count()
    assert count == 0
    assert comment_count == 0
    assert rating_count == 0


@pytest.mark.django_db
def test_image_deleted_after_update(map_idea_factory, ImagePNG):
    mapidea = map_idea_factory(image=ImagePNG)
    image_path = os.path.join(settings.MEDIA_ROOT, mapidea.image.path)
    thumbnail_path = createThumbnail(mapidea.image)

    assert os.path.isfile(image_path)
    assert os.path.isfile(thumbnail_path)

    mapidea.image = None
    mapidea.save()

    assert not os.path.isfile(image_path)
    assert not os.path.isfile(thumbnail_path)
