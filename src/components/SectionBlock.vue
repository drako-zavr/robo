<template>
      <div class="section-block" :class="bgClass">
    <div class="section-block__content w-100" >
      <div class="q-container">
        <p v-if="title" class="section-block__title  text-h4 text-secondary">
          {{ title }}
        </p>
      </div> 
      <slot></slot>
    </div>

  </div>
</template>

<script setup lang="ts">
  defineProps({
    title: String,
    bgClass: String
  });
</script>
