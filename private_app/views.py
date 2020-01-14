from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm
import logging
from django.urls import reverse_lazy
from django.contrib import messages

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy("private_app:inquiry")

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, "メッセージを送信しました。")
        logger.info("Inquiry sent by{}".format(form.cleaned_data["name"]))
        return super().form_valid(form)
