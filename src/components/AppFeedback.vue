<template>

    <form>
        <div class="row">
            <div class="col">
                <input>
            </div>
        </div>

    </form>
    <q-form>
        <q-input outlined v-model="name" label="Имя"></q-input>
        <q-input outlined v-model="phone" label="Телефон"></q-input>
        <q-input outlined v-model="email" label="E-mail"></q-input>
        <q-btn
          flat 
          type="submit"
          size="md"
          label="Оформить заявку"
        />

    </q-form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
const name = ref(''),
email = ref(''),
phone = ref('');


</script>