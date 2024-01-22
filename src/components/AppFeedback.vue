<template>
  <SectionBlock  
  bgClass="feedback-section q-pb-xl"
  >
    <div id="feedback" class="feedback q-container q-pb-xl">
      <div class="row q-mx-auto justify-around">
        <div class="feedback__desc col-6-md col-6-lg col-12-sm text-white q-px-sm q-mb-xl justify-center">
          <p class="feedback__title q-mb-md text-h4">Запишитесь на курс <br>со скидкой 10%</p>
          <p class="feedback__text text-weight-medium"> Акция действительна до 10 марта 2022 года</p>
        </div>
        <FeedbackForm />
      </div> 
    </div>

  </SectionBlock>
</template>
<script setup lang="ts">
import FeedbackForm from './FeedbackForm.vue';
import SectionBlock from './SectionBlock.vue';
</script>