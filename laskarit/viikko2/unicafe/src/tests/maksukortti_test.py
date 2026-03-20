import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20.00)
    
    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 0.00)

    def test_saldo_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_ota_rahaa_palauttaa_false(self):
        vastaus = self.maksukortti.ota_rahaa(2000)
        
        self.assertEqual(vastaus, False)

    def test_ota_rahaa_palauttaa_true(self):
        vastaus = self.maksukortti.ota_rahaa(500)

        self.assertEqual(vastaus, True)
