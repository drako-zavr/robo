<template>
  <SectionBlock bgClass="feedback-section q-pb-xl">
    <div id="feedback" class="feedback q-container q-pb-xl row q-mx-auto justify-around">
      <div>
        <p class="feedback__title q-mb-md text-h4 col-6-md col-6-lg col-12-sm text-white q-px-sm text-weight-bold">Запишитесь на курс
          <br>со скидкой 10%</p>
        <p class="feedback__text text-weight-medium col-6-md col-6-lg col-12-sm text-white q-px-sm q-mb-xl text-h6"> Акция
          действительна до 10 марта 2022 года</p>
      </div>
      <FeedbackForm />
    </div>
  </SectionBlock>
</template>
<script setup lang="ts">
import FeedbackForm from './FeedbackForm.vue';
import SectionBlock from './SectionBlock.vue';
</script>