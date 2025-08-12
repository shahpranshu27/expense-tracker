from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views import View


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = "expenses/expense_list.html"
    context_object_name = "expenses"
    ordering = ["-date"]
    paginate_by = 10

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user).order_by("-date")


class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/signup.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "registration/signup.html", {"form": form})
