import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

kejelasan_informasi = ctrl.Antecedent(np.arange(0, 100), 'kejelasan_informasi')
kejelasan_persyaratan = ctrl.Antecedent(np.arange(0, 100), 'kejelasan_persyaratan')
kemampuan_petugas = ctrl.Antecedent(np.arange(0, 100), 'kemampuan_petugas')
ketersediaan_sarpras = ctrl.Antecedent(np.arange(0, 100), 'ketersediaan_sarpras')
kepuasan_pelayanan = ctrl.Consequent(np.arange(0, 400), 'kepuasan_pelayanan')

kejelasan_informasi['Tidak Memuaskan'] = fuzz.trapmf(kejelasan_informasi.universe, [0, 0, 60, 75])
kejelasan_informasi['Cukup Memuaskan'] = fuzz.trimf(kejelasan_informasi.universe, [60, 75, 90])
kejelasan_informasi['Memuaskan'] = fuzz.trapmf(kejelasan_informasi.universe, [75, 90, 100, 100])

kejelasan_persyaratan['Tidak Memuaskan'] = fuzz.trapmf(kejelasan_persyaratan.universe, [0, 0, 60, 75])
kejelasan_persyaratan['Cukup Memuaskan'] = fuzz.trimf(kejelasan_persyaratan.universe, [60, 75, 90])
kejelasan_persyaratan['Memuaskan'] = fuzz.trapmf(kejelasan_persyaratan.universe, [75, 90, 100, 100])

kemampuan_petugas['Tidak Memuaskan'] = fuzz.trapmf(kemampuan_petugas.universe, [0, 0, 60, 75])
kemampuan_petugas['Cukup Memuaskan'] = fuzz.trimf(kemampuan_petugas.universe, [60, 75, 90])
kemampuan_petugas['Memuaskan'] = fuzz.trapmf(kemampuan_petugas.universe, [75, 90, 100, 100])

ketersediaan_sarpras['Tidak Memuaskan'] = fuzz.trapmf(ketersediaan_sarpras.universe, [0, 0, 60, 75])
ketersediaan_sarpras['Cukup Memuaskan'] = fuzz.trimf(ketersediaan_sarpras.universe, [60, 75, 90])
ketersediaan_sarpras['Memuaskan'] = fuzz.trapmf(ketersediaan_sarpras.universe, [75, 90, 100, 100])

kepuasan_pelayanan['Tidak Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [0, 0, 50, 75])
kepuasan_pelayanan['Kurang Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [50, 75, 100, 150])
kepuasan_pelayanan['Cukup Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [100, 150, 250, 275])
kepuasan_pelayanan['Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [250, 275, 325, 350])
kepuasan_pelayanan['Sangat Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [325, 350, 400, 400])

kejelasan_informasi.view()
kejelasan_persyaratan.view()
kemampuan_petugas.view()
ketersediaan_sarpras.view()
kepuasan_pelayanan.view()

aturan1 = ctrl.Rule(
    kejelasan_informasi['Cukup Memuaskan'] &
    kejelasan_persyaratan['Tidak Memuaskan'] &
    kemampuan_petugas['Tidak Memuaskan'] &
    ketersediaan_sarpras['Memuaskan'],
    kepuasan_pelayanan['Cukup Memuaskan']
)
aturan2 = ctrl.Rule(
    kejelasan_informasi['Memuaskan'] &
    kejelasan_persyaratan['Tidak Memuaskan'] &
    kemampuan_petugas['Tidak Memuaskan'] &
    ketersediaan_sarpras['Memuaskan'],
    kepuasan_pelayanan['Memuaskan']
)
aturan3 = ctrl.Rule(
    kejelasan_informasi['Tidak Memuaskan'] &
    kejelasan_persyaratan['Tidak Memuaskan'] &
    kemampuan_petugas['Tidak Memuaskan'] &
    ketersediaan_sarpras['Tidak Memuaskan'],
    kepuasan_pelayanan['Tidak Memuaskan']
)
aturan4 = ctrl.Rule(
    kejelasan_informasi['Tidak Memuaskan'] &
    kejelasan_persyaratan['Tidak Memuaskan'] &
    kemampuan_petugas['Tidak Memuaskan'] &
    ketersediaan_sarpras['Cukup Memuaskan'],
    kepuasan_pelayanan['Tidak Memuaskan']
)
aturan5 = ctrl.Rule(
    kejelasan_informasi['Tidak Memuaskan'] &
    kejelasan_persyaratan['Tidak Memuaskan'] &
    kemampuan_petugas['Tidak Memuaskan'] &
    ketersediaan_sarpras['Memuaskan'],
    kepuasan_pelayanan['Tidak Memuaskan']
)
aturan6 = ctrl.Rule(
    kejelasan_informasi['Tidak Memuaskan'] &
    kejelasan_persyaratan['Tidak Memuaskan'] &
    kemampuan_petugas['Cukup Memuaskan'] &
    ketersediaan_sarpras['Tidak Memuaskan'],
    kepuasan_pelayanan['Tidak Memuaskan']
)
aturan7 = ctrl.Rule(
    kejelasan_informasi['Tidak Memuaskan'] &
    kejelasan_persyaratan['Tidak Memuaskan'] &
    kemampuan_petugas['Cukup Memuaskan'] &
    ketersediaan_sarpras['Cukup Memuaskan'],
    kepuasan_pelayanan['Tidak Memuaskan']
)
aturan8 = ctrl.Rule(
    kejelasan_informasi['Tidak Memuaskan'] &
    kejelasan_persyaratan['Tidak Memuaskan'] &
    kemampuan_petugas['Cukup Memuaskan'] &
    ketersediaan_sarpras['Memuaskan'],
    kepuasan_pelayanan['Cukup Memuaskan']
)
aturan9 = ctrl.Rule(
    kejelasan_informasi['Tidak Memuaskan'] &
    kejelasan_persyaratan['Tidak Memuaskan'] &
    kemampuan_petugas['Memuaskan'] &
    ketersediaan_sarpras['Tidak Memuaskan'],
    kepuasan_pelayanan['Tidak Memuaskan']
)
aturan10 = ctrl.Rule(
    kejelasan_informasi['Tidak Memuaskan'] &
    kejelasan_persyaratan['Tidak Memuaskan'] &
    kemampuan_petugas['Memuaskan'] &
    ketersediaan_sarpras['Cukup Memuaskan'],
    kepuasan_pelayanan['Cukup Memuaskan']
)
aturan11 = ctrl.Rule(
    kejelasan_informasi['Tidak Memuaskan'] &
    kejelasan_persyaratan['Tidak Memuaskan'] &
    kemampuan_petugas['Memuaskan'] &
    ketersediaan_sarpras['Memuaskan'],
    kepuasan_pelayanan['Cukup Memuaskan']
)
aturan12 = ctrl.Rule(
    kejelasan_informasi['Cukup Memuaskan'] &
    kejelasan_persyaratan['Cukup Memuaskan'] &
    kemampuan_petugas['Memuaskan'] &
    ketersediaan_sarpras['Memuaskan'],
    kepuasan_pelayanan['Memuaskan']
)
aturan13 = ctrl.Rule(
    kejelasan_informasi['Cukup Memuaskan'] &
    kejelasan_persyaratan['Cukup Memuaskan'] &
    kemampuan_petugas['Memuaskan'] &
    ketersediaan_sarpras['Memuaskan'],
    kepuasan_pelayanan['Memuaskan']
)
aturan14 = ctrl.Rule(
    kejelasan_informasi['Cukup Memuaskan'] &
    kejelasan_persyaratan['Memuaskan'] &
    kemampuan_petugas['Memuaskan'] &
    ketersediaan_sarpras['Memuaskan'],
    kepuasan_pelayanan['Sangat Memuaskan']
)
aturan15 = ctrl.Rule(
    kejelasan_informasi['Memuaskan'] &
    kejelasan_persyaratan['Memuaskan'] &
    kemampuan_petugas['Memuaskan'] &
    ketersediaan_sarpras['Memuaskan'],
    kepuasan_pelayanan['Sangat Memuaskan']
)

engine = ctrl.ControlSystem([aturan1, aturan2])
system = ctrl.ControlSystemSimulation(engine)

system.input['kejelasan_informasi'] = 80
system.input['kejelasan_persyaratan'] = 60
system.input['kemampuan_petugas'] = 50
system.input['ketersediaan_sarpras'] = 90
system.compute()
print(system.output['kepuasan_pelayanan'])
kepuasan_pelayanan.view(sim=system)