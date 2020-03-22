from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Topic, Post
from django.contrib.auth.models import User

from .forms import TopicForm, ReplyForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    all_boards = Board.objects.all()
    return render(request, 'index.html', {'all_boards': all_boards})


def boards_topic(request, id):
    board = Board.objects.get(pk=id)
    return render(request, 'boards_topic.html', {'board': board})


@login_required
def new_topic(request, id):
    board = Board.objects.get(pk=id)
    user = request.user
    if request.method == 'POST':
        # subject = request.POST['subject']
        # message = request.POST['message']
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = user
            topic.save()

            post = Post.objects.create(
                topic=topic, message=form.cleaned_data.get('message'), created_by=user)

        return redirect('boards_topic', id=board.pk)
    else:
        form = TopicForm()

    return render(request, 'new_topic.html', {'board': board, 'form': form})


def topic_posts(request, id,  topic_id):
    topic = get_object_or_404(Topic, board__pk=id, pk=topic_id)
    return render(request, 'topic_posts.html', {'topic': topic})


@login_required
def reply(request, id, topic_id):
    topic = get_object_or_404(Topic, board__pk=id, pk=topic_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', id=id, topic_id=topic.pk)
    else:
        form = ReplyForm()

    return render(request, 'reply.html', {'topic': topic, 'form': form})
