<template>
  <div class="input-group mb-3">
    <span v-if="icon" class="input-group-text bg-dark text-warning border-warning">
      <i :class="`bi bi-${icon}`"></i>
    </span>
    <input
      :type="type"
      :placeholder="placeholder"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      class="form-control bg-dark text-white border-warning"
      v-bind="$attrs"
    />
  </div>
</template>

<script setup>
defineProps({
  modelValue: [String, Number],
  icon: { type: String, default: null },
  type: { type: String, default: "text" },
  placeholder: { type: String, default: "" }
})
defineEmits(['update:modelValue'])
</script>
