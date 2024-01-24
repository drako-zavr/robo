<template>
  <q-form 
  class="feedback__form col-6-md col-6-lg col-12-sm " 
  @submit="onSubmit" 
  ref="feedbackForm">
    <q-input 
    class="feedback__input q-pb-sm" 
    outlined 
    bg-color="primary" 
    v-model="name" 
    label="Имя"
      :rules="[(val) => !!val || '']">
    </q-input>
    <q-input 
    class="feedback__input q-pb-sm" 
    outlined 
    bg-color="primary" 
    v-model="phone" 
    label="Телефон"
      :rules="[(val) => !!val || '', isValidPhone()]">
    </q-input>
    <q-input 
    class="feedback__input q-pb-sm" 
    outlined 
    bg-color="primary" 
    v-model="email" 
    label="E-mail"
      :rules="[(val) => !!val || '', isValidEmail()]">
    </q-input>
    <div class="feedback__btn">
      <q-btn 
      flat
      class="feedback__btn bg-secondary q-py-md" 
      no-caps text-color="primary" 
      type="submit"
      label="Оформить заявку"/>
    </div>
  </q-form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { QForm } from 'quasar';
import { useFeedback } from 'src/composables/useFeedback';

const name = ref<string>(''),
  email = ref<string>(''),
  phone = ref<string>('');
const feedbackForm = ref<QForm>();

const isValidEmail = () => {
  const emailPattern =
    /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/;
  return (val: string) => emailPattern.test(val) || 'Неверный формат Email';
};

const isValidPhone = () => {
  const phonePattern =
    /^(?=[0-9+]{11,11}$)/;
  return (val: string) => phonePattern.test(val) || 'Неверный формат номера';
};

const onSubmit = () => {
  void feedbackForm.value?.validate().then(async (success: boolean) => {
    if (success) {
      console.log('success')
      await useFeedback(name.value,email.value,phone.value);
      name.value = '';
      email.value = '';
      phone.value = '';
    }
  });
};

</script>