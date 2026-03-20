import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_konstruktori_asettaa_myytyjen_lounaiden_maaran_oikein(self):
        self.assertEqual((self.kassapaate.edulliset) + (self.kassapaate.maukkaat), 0)

    def test_syo_edullisesti_kateisella_onnistuu(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_epaonnistuu(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_onnistuu(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_epaonnistuu(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kortilla_onnistuu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
    
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kortti.saldo_euroina(), 7.6)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_epaonnistuu(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo_euroina(), 2.0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla_onnistuu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kortti.saldo_euroina(), 6.0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_epaonnistuu(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo_euroina(), 3.0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_lataa_rahaa_kortille_onnistuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)

        self.assertEqual(self.kortti.saldo_euroina(), 15.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
    
    def test_lataa_rahaa_kortille_negatiivista_ei_muuta_mitaan(self):
        vastaus = self.kassapaate.lataa_rahaa_kortille(self.kortti,-100 )
        self.assertEqual(vastaus, None)

    def test_kassan_saldo_euroina_nakyy_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)