<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold text-blue-900 mb-6">Billing History</h1>

    <div class="bg-white rounded-xl shadow border border-gray-200 overflow-x-auto">
      <table class="min-w-full text-sm">
        <thead class="bg-gray-100 text-gray-600 uppercase text-left">
          <tr>
            <th class="px-6 py-3">Date</th>
            <th class="px-6 py-3">Plan</th>
            <th class="px-6 py-3">Amount</th>
            <th class="px-6 py-3">Payment Method</th>
            <th class="px-6 py-3">Invoice</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="bill in billingHistory"
            :key="bill.id"
            class="border-t text-gray-700"
          >
            <td class="px-6 py-4">{{ bill.date }}</td>
            <td class="px-6 py-4">{{ bill.plan }}</td>
            <td class="px-6 py-4">${{ bill.amount }}</td>
            <td class="px-6 py-4">{{ bill.method }}</td>
            <td class="px-6 py-4">
              <button
                class="text-blue-700 hover:underline"
                @click="downloadInvoice(bill.id)"
              >
                Download
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
const billingHistory = [
  {
    id: 1,
    date: "2025-03-01",
    plan: "Pro Plan",
    amount: 30,
    method: "PayPal"
  },
  {
    id: 2,
    date: "2025-02-01",
    plan: "Pro Plan",
    amount: 30,
    method: "M-PESA"
  }
];

const downloadInvoice = (id) => {
  alert(`Downloading invoice #${id}...`);
  // Badili baadaye iwe na real PDF download au link
};
</script>
