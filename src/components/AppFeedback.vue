<template>
  <SectionBlock  
  bgClass="feedback-section"
  >
    <div id="feedback" class="feedback q-container">
      <div class="feedback__row row ">
        <div class="feedback__desc col-6-md col-6-lg col-12-sm text-white q-mx-auto">
          <p class="feedback__title q-mx-auto">Запишитесь на курс <br>со скидкой 10%</p>
          <p class="feedback__text text-weight-medium q-mx-auto"> Акция действительна до 10 марта 2022 года</p>
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