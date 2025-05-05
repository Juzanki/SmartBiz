<template>
  <div class="container-fluid py-4">
    <!-- Header -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="fw-bold text-primary d-flex align-items-center gap-2">
        <i class="bi bi-credit-card-2-front-fill"></i> {{ $t("billing") }}
      </h2>
      <button class="btn btn-outline-primary" @click="goToPayments">
        <i class="bi bi-clock-history"></i> {{ $t("payment_history") }}
      </button>
    </div>

    <!-- Plans Section -->
    <div class="row g-4">
      <div v-for="plan in plans" :key="plan.name" class="col-md-4">
        <div
          class="card h-100 shadow-sm border-0 rounded-3 position-relative"
          :class="{ 'border-primary border-2': plan.name === currentPlan }"
        >
          <div class="card-body text-center">
            <h4 class="fw-bold text-primary mb-2">{{ plan.name }}</h4>
            <p class="text-muted small">{{ plan.description }}</p>
            <h2 class="fw-bold mb-3">{{ plan.price }}</h2>
            <ul class="list-unstyled mb-4 text-start">
              <li
                v-for="feature in plan.features"
                :key="feature"
                class="d-flex align-items-center gap-2 mb-2"
              >
                <i class="bi bi-check-circle-fill text-success"></i> {{ feature }}
              </li>
            </ul>
            <button
              class="btn w-100 fw-bold"
              :class="plan.name === currentPlan ? 'btn-outline-secondary' : 'btn-primary'"
              :disabled="plan.name === currentPlan"
              @click="selectPlan(plan.name)"
            >
              {{ plan.name === currentPlan ? $t("current_plan") : $t("upgrade") }}
            </button>
            <!-- PayPal Button -->
            <button
              class="btn w-100 btn-outline-success mt-3"
              @click="openPayPal(plan)"
            >
              <i class="bi bi-paypal"></i> Pay with PayPal
            </button>
            <!-- Mobile Money Button -->
            <button
              class="btn w-100 btn-outline-success mt-3"
              @click="togglePaymentMenu"
            >
              <i class="bi bi-cash-stack"></i> Pay with Mobile Money
            </button>
            <!-- Mobile Money Payment Methods -->
            <div v-if="showPaymentMethods" class="mt-3">
              <button
                class="btn btn-outline-success w-100 mb-2"
                @click="openPaymentMenu('mpesa')"
              >
                Pay with M-PESA
              </button>
              <button
                class="btn btn-outline-primary w-100 mb-2"
                @click="openPaymentMenu('airtel')"
              >
                Pay with Airtel Money
              </button>
              <button
                class="btn btn-outline-danger w-100 mb-2"
                @click="openPaymentMenu('tigo')"
              >
                Pay with Tigo Pesa
              </button>
            </div>
          </div>
          <span
            v-if="plan.name === currentPlan"
            class="badge bg-primary position-absolute top-0 end-0 m-3"
          >
            {{ $t("active") }}
          </span>
        </div>
      </div>
    </div>

    <!-- Payment Method Notes -->
    <div class="card shadow-sm border-0 rounded-3 mt-5">
      <div class="card-body">
        <h5 class="card-title fw-bold text-primary mb-3">
          <i class="bi bi-cash-stack me-2"></i> {{ $t("payment_methods") }}
        </h5>
        <div v-if="selectedMethod === 'mpesa'">
          <p><strong>Steps for M-PESA:</strong></p>
          <p>Dial *150*00# -> Select 4. Pay via M-PESA -> Select 1. Enter company number -> Enter Company Number: 5261077 -> Check the name: **UKUMBI WA MJASIRIAMALI** -> Make sure the name matches before proceeding -> Enter the amount to pay -> Enter your **M-PESA PIN** -> Confirm the payment.</p>
        </div>
        <div v-if="selectedMethod === 'airtel'">
          <p><strong>Steps for Airtel Money:</strong></p>
          <p>Dial *150*60# -> Select 5. Pay Bills -> Select 1. Enter company number -> Select 3. M-PESA -> Select 1. Enter M-PESA number -> Enter Company Number: 5261077 -> Check the name: **UKUMBI WA MJASIRIAMALI** -> Ensure the name matches before proceeding -> Enter the amount to pay -> Enter your **Airtel Money PIN** -> Confirm the payment.</p>
        </div>
        <div v-if="selectedMethod === 'tigo'">
          <p><strong>Steps for Tigo Pesa:</strong></p>
          <p>Dial *150*01# -> Select 4. Pay Bills -> Select 3. Enter company number -> Enter Company Number: 5261077 -> Check the name: **UKUMBI WA MJASIRIAMALI** -> Ensure the name matches before proceeding -> Enter the amount to pay -> Confirm with your **PIN**.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const currentPlan = ref('Pro')
const showPaymentMethods = ref(false)
const selectedMethod = ref(null)

const plans = [
  {
    name: 'Free',
    price: '$0/mo',
    description: 'Basic tools for startups and beginners.',
    features: [
      'Up to 50 messages/month',
      '1 Social platform',
      'Basic AI autoresponder',
      'Email support',
    ],
    paypalLink: 'https://www.paypal.com/ncp/payment/2YVRVNKRGVA6Q'
  },
  {
    name: 'Pro',
    price: '$9.99/mo',
    description: 'Everything you need to automate and grow.',
    features: [
      'Unlimited messages',
      'WhatsApp + Telegram + SMS',
      'Advanced AI bot & analytics',
      'Priority email support',
    ],
    paypalLink: 'https://www.paypal.com/ncp/payment/V8SA7RGZN7R3U'
  },
  {
    name: 'Business',
    price: '$29.99/mo',
    description: 'For enterprises that need full power & team access.',
    features: [
      'Everything in Pro +',
      'Team collaboration tools',
      'Multi-user dashboard',
      'Dedicated onboarding',
    ],
    paypalLink: 'https://www.paypal.com/ncp/payment/D28PZ6TYYQ24N'
  }
]

const selectPlan = (planName) => {
  alert(`Redirecting to checkout for: ${planName}`)
  // Real checkout flow integration
}

const goToPayments = () => {
  router.push('/my-payments')
}

const openPayPal = (plan) => {
  window.open(plan.paypalLink, '_blank')
}

const togglePaymentMenu = () => {
  showPaymentMethods.value = !showPaymentMethods.value
}

const openPaymentMenu = (method) => {
  selectedMethod.value = method
}
</script>

<style scoped>
.card:hover {
  transform: translateY(-4px);
  transition: all 0.3s ease;
}
.badge {
  font-size: 0.75rem;
  padding: 0.4em 0.6em;
}
</style>
