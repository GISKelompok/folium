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


kelompok4
