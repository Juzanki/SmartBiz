import { createRouter, createWebHistory } from 'vue-router'
import i18n from '../i18n'

// ========== Async Page Imports ==========
const SignupPage           = () => import('../views/SignupPage.vue')
const LoginPage            = () => import('../views/LoginPage.vue')
const ForgotPassword       = () => import('../views/ForgotPasswordPage.vue')
const VerifyCode           = () => import('../views/VerifyCode.vue')
const ResetPassword        = () => import('../views/ResetPassword.vue')
const TwoFactor            = () => import('../views/TwoFactorPage.vue')

const LandingPage          = () => import('../views/LandingPageView.vue')
const NotFound             = () => import('../views/NotFound.vue')
const Unauthorized         = () => import('../views/Unauthorized.vue')
const AccountDeleted       = () => import('../views/AccountDeleted.vue')

const DashboardAdmin       = () => import('../views/DashboardAdmin.vue')
const DashboardUser        = () => import('../views/DashboardUser.vue')
const DashboardOwner       = () => import('../views/DashboardOwner.vue')

const AutoresponderView    = () => import('../views/AutoresponderView.vue')
const AnalyticsDashboard   = () => import('../views/AnalyticsDashboard.vue')
const SettingsBranding     = () => import('../views/SettingsBranding.vue')
const UserProfileSettings  = () => import('../views/UserProfileSettings.vue')
const MessagingCenter      = () => import('../views/MessagingCenter.vue')
const ScheduledPromotions  = () => import('../views/ScheduledPromotions.vue')
const SupportCenter        = () => import('../views/SupportCenter.vue')
const LiveStreamHub        = () => import('../views/LiveStreamHub.vue')
const DroneTracker         = () => import('../views/DroneMonitor.vue')
const AffiliateDashboard   = () => import('../views/AffiliateDashboard.vue')

const MyBusiness           = () => import('../views/MyBusiness.vue')
const BusinessProfile      = () => import('../views/BusinessProfile.vue')
const Customers            = () => import('../views/Customers.vue')
const CustomerProfile      = () => import('../views/CustomerProfile.vue')
const Products             = () => import('../views/Products.vue')
const ProductProfile       = () => import('../views/ProductProfile.vue')
const Orders               = () => import('../views/Orders.vue')
const OrderProfile         = () => import('../views/OrderProfile.vue')
const PromotionProfile     = () => import('../views/PromotionProfile.vue')

// ========== New Routes to Add ==========
const Notifications        = () => import('@/views/Notifications.vue')
const LoyaltyRewards       = () => import('@/views/LoyaltyRewards.vue')
const HelpCenter           = () => import('@/views/HelpCenter.vue')
const BillingView          = () => import('@/views/BillingView.vue')
const ActivateLog          = () => import('@/views/ActivateLog.vue')
const SmartAssistant       = () => import('@/views/SmartAssistant.vue')

// ========== Route Definitions ==========
const routes = [
  { path: '/', component: LandingPage, name: 'Home' },
  { path: '/signup', component: SignupPage, name: 'Signup', meta: { guestOnly: true } },
  { path: '/login', component: LoginPage, name: 'Login', meta: { guestOnly: true } },
  { path: '/forgot-password', component: ForgotPassword, name: 'ForgotPassword', meta: { guestOnly: true } },
  { path: '/verify-code', component: VerifyCode, name: 'VerifyCode', meta: { guestOnly: true } },
  { path: '/reset-password', component: ResetPassword, name: 'ResetPassword', meta: { guestOnly: true } },
  { path: '/two-factor', component: TwoFactor, name: 'TwoFactor', meta: { requires2FA: true } },
  { path: '/account-deleted', component: AccountDeleted, name: 'AccountDeleted', meta: { guestOnly: true } },

  {
    path: '/dashboard',
    name: 'Dashboard',
    beforeEnter: (to, from, next) => {
      const role = localStorage.getItem('user_role')
      if (role === 'owner') return next('/dashboard/owner')
      if (role === 'admin') return next('/dashboard/admin')
      if (role === 'user') return next('/dashboard/user')
      return next('/login')
    }
  },

  { path: '/dashboard/user', component: DashboardUser, name: 'DashboardUser', meta: { requiresAuth: true, requiresRole: 'user' } },
  { path: '/dashboard/admin', component: DashboardAdmin, name: 'DashboardAdmin', meta: { requiresAuth: true, requiresRole: 'admin' } },
  { path: '/dashboard/owner', component: DashboardOwner, name: 'DashboardOwner', meta: { requiresAuth: true, requiresRole: 'owner' } },

  { path: '/autoresponder', component: AutoresponderView, name: 'Autoresponder', meta: { requiresAuth: true } },
  { path: '/analytics', component: AnalyticsDashboard, name: 'Analytics', meta: { requiresAuth: true } },
  { path: '/settings', component: SettingsBranding, name: 'Settings', meta: { requiresAuth: true } },
  { path: '/profile', component: UserProfileSettings, name: 'UserProfile', meta: { requiresAuth: true } },
  { path: '/messaging-center', component: MessagingCenter, name: 'MessagingCenter', meta: { requiresAuth: true } },
  { path: '/scheduled-promotions', component: ScheduledPromotions, name: 'ScheduledPromotions', meta: { requiresAuth: true } },
  { path: '/support', component: SupportCenter, name: 'Support', meta: { requiresAuth: true } },
  { path: '/live-stream', component: LiveStreamHub, name: 'LiveStreamHub', meta: { requiresAuth: true } },
  { path: '/drone_tracking', component: DroneTracker, name: 'DroneTracking', meta: { requiresAuth: true } },
  { path: '/affiliate', component: AffiliateDashboard, name: 'AffiliateDashboard', meta: { requiresAuth: true } },

  { path: '/notifications', component: Notifications, name: 'Notifications', meta: { requiresAuth: true } },
  { path: '/loyalty_rewards', component: LoyaltyRewards, name: 'LoyaltyRewards', meta: { requiresAuth: true } },
  { path: '/help', component: HelpCenter, name: 'HelpCenter', meta: { requiresAuth: true } },
  { path: '/billing', component: BillingView, name: 'Billing', meta: { requiresAuth: true } },
  { path: '/activate_log', component: ActivateLog, name: 'ActivateLog', meta: { requiresAuth: true } },
  { path: '/smart_assistance', component: SmartAssistant, name: 'SmartAssistant', meta: { requiresAuth: true } },

  { path: '/my-business', component: MyBusiness, name: 'MyBusiness', meta: { requiresAuth: true } },
  { path: '/business-profile/:id', component: BusinessProfile, name: 'BusinessProfile', meta: { requiresAuth: true } },
  { path: '/customers', component: Customers, name: 'Customers', meta: { requiresAuth: true } },
  { path: '/customer-profile/:id', component: CustomerProfile, name: 'CustomerProfile', meta: { requiresAuth: true } },
  { path: '/products', component: Products, name: 'Products', meta: { requiresAuth: true } },
  { path: '/product-profile/:id', component: ProductProfile, name: 'ProductProfile', meta: { requiresAuth: true } },
  { path: '/orders', component: Orders, name: 'Orders', meta: { requiresAuth: true } },
  { path: '/order-profile/:id', component: OrderProfile, name: 'OrderProfile', meta: { requiresAuth: true } },
  { path: '/promotion-profile/:id', component: PromotionProfile, name: 'PromotionProfile', meta: { requiresAuth: true } },

  { path: '/unauthorized', component: Unauthorized, name: 'Unauthorized' },
  { path: '/:pathMatch(.*)*', component: NotFound, name: 'NotFound' }
]

// ========== Router Setup ==========
const router = createRouter({
  history: createWebHistory(),
  routes
})

// ========== Route Guards ==========
router.beforeEach((to, from, next) => {
const lang = localStorage.getItem('user\_lang') || 'en'
i18n.global.locale = lang

const token = localStorage.getItem('access\_token')
const rawRole = localStorage.getItem('user\_role') || ''
const role = rawRole.toLowerCase().trim() // 💡 Normalize role to lowercase
const needs2FA = localStorage.getItem('needs\_2fa') === 'true'

console.log("🔐 Role in localStorage:", role)
console.log("🔐 Route requires:", to.meta.requiresRole)

// 👤 Already logged in? Redirect away from guest pages
if (to.meta.guestOnly && token) return next('/dashboard')

// 🔒 Requires auth but no token
if (to.meta.requiresAuth && !token) return next('/login')

// 🔐 Requires 2FA but not verified
if (to.meta.requires2FA && (!token || !needs2FA)) return next('/login')

// 👮 Requires specific role — Owner has full access
if (to.meta.requiresRole && role !== to.meta.requiresRole && role !== 'owner') {
  return next('/unauthorized')
}

return next()
})

export default router
