<template>
  <q-card class="package-card flex column no-box-shadow q-pa-none q-mx-md q-mb-lg">

    <q-card-section class="package-card__content col q-pa-none">
      <p class="package-card__title text-center text-h4 q-mt-xl q-mb-xl q-pb-xl text-weight-medium">- {{ pack?.name }} -</p>
      <p class="text-center text-h3 q-mb-lg text-weight-medium">{{ pack?.price }} ₽</p>
      <p class="package-card__text text-center q-mx-auto q-mb-xl text-body1">{{ pack?.desc }}</p>
      <q-btn no-caps flat name="isactive" class="package-card__btn text-white bg-accent q-mx-xl q-mb-xl q-px-xl q-py-lg text-body1"
        href="#feedback">Оставить заявку</q-btn>
    </q-card-section>

  </q-card>
</template>
<script setup lang="ts">
import { Package } from 'src/models/package';
import { PropType } from 'vue';

defineProps({
  pack: Object as PropType<Package>
});

</script>