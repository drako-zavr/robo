<template>
  <div class="section-block" :class="bgClass">
    <div class="w-100 q-container">
      <p v-if="title" class="section-block__title  text-h4 text-secondary text-weight-bold q-mb-xl">
        {{ title }}
      </p>
    </div>
    <slot></slot>
  </div>
</template>
<script setup lang="ts">
defineProps({
  title: String,
  bgClass: String
});
</script>