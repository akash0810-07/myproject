from django.shortcuts import get_object_or_404, redirect, render

from .forms import MemberForm
from .models import Member


def home(request):
    all_members = Member.objects.all()
    return render(request, "home.html", {"all": all_members})


def update_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)

    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MemberForm(instance=member)

    return render(request, "member_form.html", {"form": form, "member": member})


def delete_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)

    if request.method == "POST":
        member.delete()
        return redirect("home")

    return render(request, "member_confirm_delete.html", {"member": member})
