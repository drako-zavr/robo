<template>
  <q-page class="index-page">
    <AppHeader/>
    <AppExample/>
    <AppFeedback/>
  </q-page>
</template>

<script setup lang="ts">
import AppExample from 'components/AppExample.vue'
import AppFeedback from 'src/components/AppFeedback.vue';
import AppHeader from 'src/components/AppHeader.vue';
</script>
