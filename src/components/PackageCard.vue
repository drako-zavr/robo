<template>
    <q-card class="package-card flex column justify-start q-pa-md">

        <q-card-section class="package-card__content col">
                    <p class="package-card__title text-center text-h4">- {{ pack?.name }} -</p>
                    <p class="package-card__price text-center">{{ pack?.price }} ₽</p>
                    <p class="package-card__details text-center">{{ pack?.desc }}</p>
                    <q-btn no-caps name="isactive" class="package-card__btn text-white bg-accent q-mx-auto" href="#feedback">Оставить заявку</q-btn>
        </q-card-section>
 
    </q-card>
</template>
<script setup lang="ts">
import { Package } from 'src/models/package';
import { PropType} from 'vue';

  defineProps({
  pack: Object as PropType<Package>
});

</script>