from django.shortcuts import render ,redirect , get_object_or_404
from django.http import HttpResponse
from .models import Note , Comment
from .forms import AddNote , AddComment
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.models import Profile
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import  LoginRequiredMixin , UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.
#  show all notes
def all_notes(request):
    user = request.user
    all_notes = Note.objects.filter(user=user)
    profile = get_object_or_404(Profile , user=user)
    numNotes = all_notes.count()
    
    context = {
        'numNotes':numNotes,
        'all_notes': all_notes,
        'profile':profile,
    }
    return render(request, 'notes.html', context)

#  show one note
def details(request,slug):
    user = request.user
    note = Note.objects.get(slug=slug)
    profile = get_object_or_404(Profile , user=user)
    note = Note.objects.get(slug=slug)
    all_comments = Comment.objects.filter(noteComment=note) 
    count = all_comments.count()
    # up = note.user.username.upper()
    context = {
        'note': note,
        'profile':profile,
        'count':count,
    }
    return render(request, 'one_note.html',context)
    
    
#  delete note
class Delete( UserPassesTestMixin, LoginRequiredMixin ,DeleteView):
    
    model = Note
    context_object_name = 'note'
    success_url = "/"
    template_name = 'delete_note.html'
    def test_func(self):
        note = self.get_object()
        if self.request.user == note.user:
            return True
        else:
            return False

# add note form 
def add_note(request):
    if request.method == 'POST':
        
        form  = AddNote(request.POST,request.FILES)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.user = request.user
            form.save()
            messages.info(request, 'Note created successfully')
            return redirect('/notes')
            


            
    else:
        form  = AddNote() 
        
    user = request.user 
    profile = get_object_or_404(Profile , user=user)    
    context = {
        'form': form,
        'profile':profile,
    }
    # Create a toast notification
    # toaster = win10toast.ToastNotifier()
    # toaster.show_toast("Hello", "you Can add note now", duration=10)
    return render(request, 'add_note.html', context)
    

#  Add CommentForm
def add_Comment(request,slug):
    if request.method == 'POST':
        note =get_object_or_404(Note , slug = slug)
        
        all_comments = Comment.objects.filter(noteComment=note)
        comment_form  = AddComment(request.POST)
        if comment_form.is_valid():
            newForm = comment_form.save(commit=False)
            newForm.user = request.user
            newForm.noteComment = note
            comment_form.save()
            # newForm.comment = ''
            messages.info(request, 'Comment created successfully')
            
            
    else:
        note = Note.objects.get(slug=slug)
        all_comments = Comment.objects.filter(noteComment=note)
        comment_form  = AddComment() 
    user = request.user 
    profile = get_object_or_404(Profile , user=user)   
    count = all_comments.count()
    context = {
        'count':count,
        'all_comments': all_comments,
        'comment_form': comment_form,
        'profile':profile,
        'note': note,
    }
    return render(request, 'comment.html', context)
    
### 
#  delete COmment
# class DeleteComment( UserPassesTestMixin, LoginRequiredMixin ,DeleteView):
    
#     model = Comment
#     context_object_name = 'comment'
#     success_url = "/"
#     template_name = 'delete_comment.html'
#     def test_func(self):
#         comment = self.get_object()
#         if self.request.user == comment.user:
#             return True
#         else:
#             return False

###########
def edit(request,slug):
    note =get_object_or_404(Note , slug = slug)
    if request.method == 'POST':
        
        form  = AddNote(request.POST,request.FILES , instance=note)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.user = request.user
            form.save()
            messages.info(request, 'Note Updated successfully')
            return redirect('/notes')
    else:
        form  = AddNote(instance=note)
        
        user = request.user 
    profile = get_object_or_404(Profile , user=user)       
    context = {
        'note':note,
        'form': form,
        'profile':profile,
    }
    return render(request, 'create.html', context)