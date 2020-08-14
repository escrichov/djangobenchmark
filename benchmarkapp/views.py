from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Benchmark, BenchmarkDetail


def view_index(request):
    content = '''
    <h1>URLS</h1>
    <a href="/benchmark/json/">benchmark json</p>
    <a href="/benchmark/render/">benchmark render</p>
    <a href="/benchmark/model/">benchmark model</p>
    '''
    return HttpResponse(content)


def view_json(request):
    return HttpResponse(json.dumps({
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6
    }), content_type='application/json')

def view_render(request):
    return render(request, 'benchmarkapp/index.html', {
        'title': 'Benchmark',
        'description': 'Benchmark description',
        'content': '<p>Hello world! This is HTML5 Boilerplate.</p>'
    })


def view_model(request):
    benchmark_detail = BenchmarkDetail()
    benchmark_detail.description = 'Benchmark Detail description'
    benchmark_detail.name = 'benchmark detail name'
    benchmark_detail.save()

    benchmark = Benchmark()
    benchmark.description = 'Benchmark description'
    benchmark.name = 'benchmark name'
    benchmark.benchmark_detail = benchmark_detail
    benchmark.save()

    benchmark_from_db = Benchmark.objects.get(id=benchmark.id)

    return HttpResponse(json.dumps({
        'benchmark': {
            'name': benchmark_from_db.name,
            'description': benchmark_from_db.description,
            'benchmark_detail': {
                'name': benchmark_from_db.benchmark_detail.name,
                'description': benchmark_from_db.benchmark_detail.description,
            }
        }
    }))
