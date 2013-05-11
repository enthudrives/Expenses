from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import loader, Context, RequestContext
from django.views.generic import DetailView
from Expenses.models import Expense, ExpenseForm, ExpenseSheet, ExpenseSheetForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render



@login_required(login_url="login")
def index(request):
    expense_sheets = ExpenseSheet.objects.filter(created_by=request.user.id);
    template = loader.get_template('Expenses/index.html')
    context = Context({
        "expense_sheets": expense_sheets
    })
    return HttpResponse(template.render(context))


@login_required(login_url="login")
def new(request):
    expense_sheet = ExpenseSheetForm()
    return render_to_response('Expenses/new.html', RequestContext(request,{'expense_sheet': expense_sheet}))


@login_required(login_url="login")
def create(request):
    if request.method == 'POST':
        expense_sheet = ExpenseSheetForm(request.POST)
        expense_sheet.instance.created_by = request.user
        expense_sheet.save()
    return redirect('index')


@login_required(login_url="login")
def add_row(request, pk):
    if request.method == 'POST':
        expense_row = ExpenseForm(request.POST)
        expense_row.instance.created_by_id = request.user.id
        expense_sheet = ExpenseSheet.objects.get(pk=pk)
        expense_row.instance.belongs_to_sheet_id = expense_sheet.id
        expense_row.save()
        expense_sheet.total += expense_row.cleaned_data['amount']
        expense_sheet.save()

    return redirect('/expense/'+pk)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render_to_response( "accounts/register.html", RequestContext(request, {
        'form': form,
        }))


class ExpenseSheetDetail(DetailView):
    model = ExpenseSheet
    context_object_name = "expensesheet"

    def get_context_data(self, **kwargs):
        context = super(ExpenseSheetDetail, self).get_context_data(**kwargs)
        context['expenses'] = Expense.objects.filter(belongs_to_sheet=context['expensesheet'])
        context['expense_row_form'] = ExpenseForm()
        return context


