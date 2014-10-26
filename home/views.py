import xml.etree.ElementTree as ET

from django.shortcuts import get_object_or_404, render
from home import sql_handler

#from home.models import Question

#from django.http import HttpResponse
log_entries = []
list_entries = []
post_count = 0


def index(request):
    context = {}
    return render(request, 'home/index.html', context)

def post(request):
    tree = ET.parse('svn_log.xml')
    root = tree.getroot()

    for child in root:
        log_entries.append(dict({'revision' : child.attrib['revision'],
                                 'author' : child[0].text,
                                 'paths' : child[2],
                                 'date' : child[1].text,
                                 'message' : child[3].text}))

    tree = ET.parse('svn_list.xml')
    root = tree.getroot()

    for child in root:
        for child1 in child:
            if(child1.attrib['kind'] == "file"):
                list_entries.append(dict({'name' : child1[0].text,
                                          'size' : child1[1].text,
                                          'revision' : child1[2].attrib['revision'],
                                          'author' : child1[2][0].text,
                                          'date' : child1[2][1].text,
                                          'kind' : child1.attrib['kind']}))
            else:
                list_entries.append(dict({'name' : child1[0].text,
                                          'revision' : child1[1].attrib['revision'],
                                          'author' : child1[1][0].text,
                                          'date' : child1[1][1].text,
                                          'kind' : child1.attrib['kind']}))
    context = {}
    if(request.GET.get('Post')):
        global post_count
        txt = sql_handler.insert(post_count, post_count, request.GET.get('commentBox'), "Anne")
        post_count+=1
        print(post_count)
        context['comment'] = txt
        return render(request, 'home/post.html', context)

    i=0
    for e in list_entries:
        if e['kind'] == 'dir' and '/' not in e['name']:
            key = 'project_' + str(i)
            context[key] = e['name']
            key = 'revision_' + str(i)
            context[key] = e['revision']
            key = 'author_' + str(i)
            context[key] = e['author']
            key = 'date_' + str(i)
            context[key] = e['date']
            i+=1

    return render(request, 'home/post.html', context)

def project0(request):
    context = {}
    list = []
    rev_list = []
    prev_revs = []
    i=0
    for e in list_entries:
        if e['kind'] == 'file' and 'Assignment1.0' in e['name']:
            list.append(dict({'name' : e['name'], 'size' : e['size'],
                              'path' : "https://subversion.ews.illinois.edu/svn/fa14-cs242/aomclau2/" + e['name']}))

        for entry in log_entries:
            file_path = e['name']
            for p in entry['paths']:
                if entry['revision'] not in prev_revs and file_path in p.text:
                    prev_revs.append(entry['revision'])
                    rev_list.append(dict({'name' : entry['revision'], 'author' : entry['author'],
                                          'date' : entry['date'], 'msg' : entry['message']}))
    context['list'] = list
    context['rev_list'] = rev_list
    return render(request, 'home/post.html', context)

def about(request):
    context = {}
    return render(request, 'home/about.html', context)

def contact(request):
    context = {}
    return render(request, 'home/contact.html', context)

'''def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'home/detail.html', {'question': question})'''