import uuid

from django.db import models,

# Create your models here.

ganjil = "Ganjil"
genap = "Genap"

SEMESTER = (
    (ganjil, "Ganjil"),
    (genap, "Genap"),
)

#tabel referensi
class agama (models.Model):
    id_agama = models.UUIDField(primary_key=True, default=uuid.uuid4, null=True)
    nm_agama
class semester (models.Model):
    id_smt = models.UUIDField(primary_key=True, default=uuid.uuid4, null=True)
    id_thn_ajaran
    nm_smt
    smt
    a_periode_aktif
    tgl_mulai
    tgl_selesai


class bentuk_pendidikan(models.Model):
    id_bp = models.UUIDField(primary_key=True, default=uuid.uuid4, null=True)
    nm_bp
    a_jenj_paud
    a_jenj_tk
    a_jenj_sd
    a_jenj_smp
    a_jenj_sma
    a_jenj_tinggi
    dir_bina
    a_aktif

class tahun_ajaran(models.Model):
    id_thn_ajaran = models.UUIDField(primary_key=True, default=uuid.uuid4, null=True)
    nm_thn_ajaran
    a_periode_aktif
    tgl_mulai
    tgl_selesai

class kurikulum(models.Model):
    id_kurikulum_sp = models.UUIDField(primary_key=True, default=uuid.uuid4, null=True)
    id_sms
    id_jenj_didik
    id_smt
    nm_kurikulum_sp
    jml_sem_normal
    jml_sks_lulus
    jml_sks_wajib
    jml_sks_pilihan


class kuliah_mahasiswa(models.Model):
    id_smt
    id_reg_pd
    id_stat_mhs
    ips
    sks_smt
    ipk
    sks_total

class mahasiswa(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)

    def __str__(self):
        return '%s, %s' % (self.nim, self.nama)


class mata_kuliah(models.Model):
    id_mk
    id_sms
    id_jenj_didik
    kode_mk
    nm_mk
    jns_mk
    kel_mk
    sks_mk
    sks_tm
    sks_prak
    sks_prak_lap
    sks_sim
    metode_pelaksanaan_kuliah
    a_sap
    a_silabus
    a_bahan_ajar
    acara_prak
    a_diktat
    tgl_mulai_efektif
    tgl_akhir_efektif

    def __str__(self):
        return '%s, %s' % (self.kode_matkul, self.nama_matkul)

class mata_kuliah_kurikulum(models.Model):
    id_kurikulum_sp
    id_mk
    smt
    sks_mk
    sks_tm
    sks_prak
    sks_prak_lap
    sks_sim
    a_wajib


class krs(models.Model):
    nim = models.ForeignKey(mahasiswa, on_delete=models.CASCADE)
    kode_matkul = models.ForeignKey(matkul, on_delete=models.CASCADE)
    semester = models.CharField(choices=SEMESTER, max_length=50)
    #Kurikulum = models.ForeignKey(kurikulum,on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.nim, self.kode_matkul)
