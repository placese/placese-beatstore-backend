from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from beatstore.models import Beat
from beatstore.serializers import BeatSerializer


class BeatApiTestCase(APITestCase):
    def setUp(self):
        self.beat_1 = Beat.objects.create(name='NYLON', price_wav='1000', price_track_out='1500',
                                          price_exclusive='5000',
                                          cover='cover.jpg',
                                          track='nylon.wav')

    def test_get(self):
        url = reverse('beat-list')
        response = self.client.get(url)
        serializer_data = BeatSerializer(self.beat_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        serializer_data['cover'] = 'http://testserver/cover.jpg'
        serializer_data['track'] = 'http://testserver/nylon.wav'
        print('------------------------------------------')
        print(serializer_data)
        print('------------------------------------------')
        print(response.data)
        print('------------------------------------------')
        # self.assertEqual(serializer_data, response.data)

