<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const adminName = ref('Admin')

// 🌐 Role Guard ndani ya component
onMounted(() => {
  const token = localStorage.getItem('access_token')
  const role = (localStorage.getItem('user_role') || '').toLowerCase().trim()
  const name = localStorage.getItem('user_name') || 'Admin'

  if (!token) {
    return router.push('/login')
  }
  if (role !== 'admin') {
    return router.push('/unauthorized')
  }

  adminName.value = name
})

const stats = [
  { title: "Total Users", value: "1,254", icon: "👥" },
  { title: "Active Subscriptions", value: "843", icon: "💼" },
  { title: "Payments Today", value: "$2,540", icon: "💳" },
  { title: "Pending Verifications", value: "12", icon: "⏳" },
]

const management = [
  {
    title: 'Manage Users',
    desc: 'View, update roles, or suspend user accounts.',
    icon: '👥',
    route: '/admin/users',
    actionText: 'View Users'
  },
  {
    title: 'Manage Payments',
    desc: 'Track all user transactions and subscriptions.',
    icon: '💳',
    route: '/admin/payments',
    actionText: 'View Payments'
  },
  {
    title: 'Manage Plans',
    desc: 'Update pricing plans like Free, Pro, and Business.',
    icon: '📝',
    route: '/admin/plans',
    actionText: 'Manage Plans'
  },
  {
    title: 'System Settings',
    desc: 'Adjust global settings and configurations.',
    icon: '⚙️',
    route: '/admin/settings',
    actionText: 'System Settings'
  }
]

const navLinks = [
  { name: "overview", label: "Overview", path: "/dashboard/admin", icon: "🏠" },
  { name: "users", label: "Users", path: "/admin/users", icon: "👥" },
  { name: "payments", label: "Payments", path: "/admin/payments", icon: "💳" },
  { name: "plans", label: "Plans", path: "/admin/plans", icon: "📝" },
  { name: "settings", label: "Settings", path: "/admin/settings", icon: "⚙️" },
]
</script>
