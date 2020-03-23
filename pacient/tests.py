# Create your tests here.
import unittest

from django.contrib.auth.models import User

from collaborator.models import Profile
from pacient.models import Pacient


class PacientesEusuarios(unittest.TestCase):

    def setUp(self):
        # """User"""
        # self.user1 = User.objects.create_user(first_name='usuario Teste1',
        #                                       username='usuarioteste1',
        #                                       is_staff='1',
        #                                       email=None,
        #                                       password='admin')
        #
        # self.user2 = User.objects.create_user(first_name='usuario Teste2',
        #                                       username='usuarioteste2',
        #                                       is_staff='1',
        #                                       email=None,
        #                                       password='admin')
        #
        # self.user3 = User.objects.create_user(first_name='usuario Teste3',
        #                                       username='usuarioteste3',
        #                                       is_staff='1',
        #                                       email=None,
        #                                       password='admin')
        #
        # """Profile"""
        # self.profile = Profile.objects.create(user_id='22',
        #                                       nome='admin',
        #                                       )

        """Patient"""
        self.pacient1 = Pacient.objects.create(name='pacient 1',
                                               email='ciceroregis25@mail.com',
                                               date_of_birth='2020-03-20',
                                               sexo='M')

        self.pacient2 = Pacient.objects.create(name='pacient 2',
                                               email='ciceroregis25@mail.com',
                                               date_of_birth='2020-03-20',
                                               sexo='M')

        self.pacient3 = Pacient.objects.create(name='pacient 3',
                                               email='ciceroregis25@mail.com',
                                               date_of_birth='2020-03-20',
                                               sexo='M')
        self.pacient4 = Pacient.objects.create(name='pacient 4',
                                               email='ciceroregis25@mail.com',
                                               date_of_birth='2020-03-20',
                                               sexo='M')

        self.pacient5 = Pacient.objects.create(name='pacient 5',
                                               email='ciceroregis25@mail.com',
                                               date_of_birth='2020-03-20',
                                               sexo='M')

        # print('User', self.users)
        print('pacient1', self.pacient1)
        print('pacient2', self.pacient2)
        print('pacient3', self.pacient3)
        print('pacient4', self.pacient4)
        print('pacient5', self.pacient5)

    def test_lista_dados_pacient_usuario(self):
        self.user = Profile.objects.all()

        if self.user:
            print('usuarios', self.user)
