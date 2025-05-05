<template>
  <div class="container py-5">
    <!-- Heading for Help Center -->
    <h2 class="text-center text-primary mb-4">Help Center</h2>
    <p class="text-center text-muted mb-5">Find answers to your most common questions below. If you need further assistance, feel free to reach out!</p>

    <!-- FAQ Section -->
    <div class="accordion" id="faqAccordion">
      <div v-for="(faq, index) in faqs" :key="index" class="accordion-item">
        <h2 class="accordion-header" :id="'heading' + index">
          <button
            class="accordion-button"
            type="button"
            data-bs-toggle="collapse"
            :data-bs-target="'#collapse' + index"
            aria-expanded="true"
            :aria-controls="'collapse' + index"
          >
            {{ faq.question }}
          </button>
        </h2>
        <div
          :id="'collapse' + index"
          class="accordion-collapse collapse"
          :aria-labelledby="'heading' + index"
          data-bs-parent="#faqAccordion"
        >
          <div class="accordion-body">
            {{ faq.answer }}
          </div>
        </div>
      </div>
    </div>

    <!-- Contact Form -->
    <div class="mt-5">
      <h5 class="text-center text-primary">Still Need Help? Reach Out to Us!</h5>
      <form @submit.prevent="submitContactForm">
        <div class="mb-3">
          <label for="subject" class="form-label">Subject</label>
          <input type="text" id="subject" class="form-control" v-model="contactForm.subject" required placeholder="Enter the subject" />
        </div>
        <div class="mb-3">
          <label for="message" class="form-label">Message</label>
          <textarea id="message" class="form-control" v-model="contactForm.message" rows="4" required placeholder="Describe your issue or question"></textarea>
        </div>
        <div class="d-flex justify-content-end">
          <button type="submit" class="btn btn-primary">
            <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
            Send Message
          </button>
        </div>
      </form>
      <div v-if="successMessage" class="alert alert-success mt-3" role="alert">
        {{ successMessage }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelpCenter',
  data() {
    return {
      // Example FAQ data
      faqs: [
        {
          question: 'How can I reset my password?',
          answer: 'To reset your password, click on "Forgot Password" on the login page and follow the instructions.',
        },
        {
          question: 'How do I contact support?',
          answer: 'You can reach out to support by filling the contact form below or by emailing us at support@example.com.',
        },
        {
          question: 'Can I upgrade my subscription?',
          answer: 'Yes, you can upgrade your subscription by visiting the "Account Settings" page and selecting the "Upgrade Plan" option.',
        },
      ],
      // Contact form data
      contactForm: {
        subject: '',
        message: '',
      },
      loading: false,
      successMessage: '',
    };
  },
  methods: {
    submitContactForm() {
      this.loading = true;
      this.successMessage = '';

      // Simulating sending the message
      setTimeout(() => {
        this.loading = false;
        this.successMessage = 'Your message has been sent successfully!';
        this.contactForm.subject = '';
        this.contactForm.message = '';
      }, 2000);
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 960px;
  margin: auto;
}

.text-center {
  text-align: center;
}

.accordion-button {
  font-weight: bold;
}

.accordion-body {
  background-color: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 0.375rem;
}

.form-label {
  font-weight: 600;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
}

.mb-5 {
  margin-bottom: 3rem;
}

.mb-3 {
  margin-bottom: 1.5rem;
}

.spinner-border {
  border-color: #ffffff;
}

.alert {
  font-size: 0.875rem;
}
</style>
