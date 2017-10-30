#!/bin/python

import folium

kelompok4 = folium.Map(
    location=[-7.7736179,110.3581032],
    zoom_start=12,
    tiles='Stamen Terrain'
)
folium.Marker([-7.773970, 110.378737], popup='<i>Museum UGM</i>').add_to(kelompok4)
folium.Marker([-7.773458, 110.378980], popup='<i>Masjid Kampus UGM</i>').add_to(kelompok4)
folium.Marker([-7.774330, 110.376871], popup='<i>Gelanggang Mahasiswa</i>').add_to(kelompok4)
folium.Marker([-7.772782, 110.377068], popup='<i>Pusat Kebudayaan Koesnadi Hardjasoemantri UGM</i>').add_to(kelompok4)
folium.Marker([-7.772196, 110.379480], popup='<i>Fakultas Ilmu Budaya UGM</i>').add_to(kelompok4)
folium.Marker([-7.774376, 110.376051], popup='<i>Sekolah Vokasi Universitas Gadjah Mada</i>').add_to(kelompok4)
folium.Marker([-7.772271, 110.379617], popup='<i>Pusat Pelatihan Bahasa UGM</i>').add_to(kelompok4)
folium.Marker([-7.770692, 110.380315], popup='<i>Fakultas Ekonomika dan Bisnis UGM</i>').add_to(kelompok4)
folium.Marker([-7.770181, 110.378661], popup='<i>Grha Sabha Pramana UGM</i>').add_to(kelompok4)
folium.Marker([-7.770049, 110.381663], popup='<i>Fakultas Hukum UGM</i>').add_to(kelompok4)

folium.Marker([-7.7834434,110.3208186], popup='<i>Toko Sahabat</i>').add_to(kelompok4)
folium.Marker([-7.7837716,110.3221678], popup='<i>Warung Makan Nasi Rames Bu Sri</i>').add_to(kelompok4)
folium.Marker([-7.7837716,110.3216206], popup='<i>Rumah Makan Padang Murah</i>').add_to(kelompok4)
folium.Marker([-7.7837357,110.322369], popup='<i>Sup Buah Dan Es Campur Cak Adi</i>').add_to(kelompok4)
folium.Marker([-7.7837613,110.322894], popup='<i>Cafe Via</i>').add_to(kelompok4)
folium.Marker([-7.7839414,110.3229101], popup='<i>Gessa Cake</i>').add_to(kelompok4)
folium.Marker([-7.7838885,110.3229671], popup='<i>Chinese Food Kasih Karunia (KK)</i>').add_to(kelompok4)
folium.Marker([-7.7848994,110.3230408], popup='<i>Mie Ayam " Bu Tini "</i>').add_to(kelompok4)
folium.Marker([-7.785114,110.3230952], popup='<i>Soto & Bakso Pak Pagi</i>').add_to(kelompok4)
folium.Marker([-7.7856827,110.3229463], popup='<i>Mava Masakan Padang</i>').add_to(kelompok4)

kelompok4
