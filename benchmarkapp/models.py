from django.db import models


class BenchmarkDetail(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=32)


class Benchmark(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=32)

    benchmark_detail = models.ForeignKey(BenchmarkDetail, on_delete=models.CASCADE)
