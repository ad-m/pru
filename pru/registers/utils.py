from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def sorter(request, queryset, order_fields):
    order_dir = request.GET.get('order', 'asc')
    print order_dir
    order_by = request.GET.get('order_by', None)
    print order_by
    order_key = order_fields.get(order_by, order_fields.values()[0])
    print order_key
    if order_dir == 'desc':
        order_key = '-'+order_key
    return queryset.order_by(order_key)


def paginator(request, queryset, per_page=25):
    per_page = request.GET.get('per_page', per_page)

    paginator = Paginator(queryset, per_page)
    page = request.GET.get('page')
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        return paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        return paginator.page(paginator.num_pages)


def serializer(obj, fields):
    record = {}
    for x in fields:
        data = getattr(obj, x)
        record[x] = data() if callable(data) else data
    return record


def serializer_page(page, fields):
    results = {}
    results['paginator'] = {'total': page.paginator.count, 'num_pages': page.paginator.num_pages}
    results['results'] = [serializer(obj, fields) for obj in page]
    return results
