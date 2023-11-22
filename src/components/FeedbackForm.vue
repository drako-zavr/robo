<template>
    <q-form @submit.prevent="onSubmit" ref="feedbackForm" >
        <q-input 
        outlined 
        bg-color="primary" 
        v-model="name" 
        label="Имя" 
        :rules="[(val) => !!val || 'Обязательное поле']">
      </q-input>
        <q-input 
        outlined 
        bg-color="primary"
        v-model="phone" 
        label="Телефон" 
        :rules="[(val) => !!val || 'Обязательное поле', isValidPhone()]"></q-input>
        <q-input 
        outlined 
        bg-color="primary"
        v-model="email" 
        label="E-mail" 
        :rules="[(val) => !!val || 'Обязательное поле', isValidEmail()]"
        ></q-input>
        <q-btn   
          text-color="primary"
          type="submit"
          size="md"
          label="Оформить заявку"
          color="secondary" 
        />
    </q-form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { api } from 'boot/axios';
import { QForm } from 'quasar';



const name = ref(''),
email = ref(''),
phone = ref('');
const feedbackForm = ref<QForm>();//?

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
      
      await api
        .post('/feedback/create/', {
          name: name.value,
          email: email.value,
          phone: phone.value
        })
        .catch((e) => {
          console.error(e);
          
        });
    }
  });
};

</script>