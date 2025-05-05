<template>
  <div class="input-group mb-3">
    <span v-if="icon" class="input-group-text bg-dark text-warning border-warning">
      <i :class="`bi bi-${icon}`"></i>
    </span>
    <select
      :value="modelValue"
      @change="$emit('update:modelValue', $event.target.value)"
      class="form-select bg-dark text-white border-warning"
      v-bind="$attrs"
    >
      <option v-for="option in options" :key="option.value" :value="option.value">
        {{ option.label }}
      </option>
    </select>
  </div>
</template>

<script setup>
defineProps({
  modelValue: [String, Number],
  icon: { type: String, default: null },
  options: { type: Array, default: () => [] }
})
defineEmits(['update:modelValue'])
</script>
