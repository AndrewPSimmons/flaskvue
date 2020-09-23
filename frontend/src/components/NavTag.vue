<template>
  <div>
    <!-- The RouterLinks are treated as <a></a> tags once rendered! -->
    <router-link id="tag" class="nav-link" :to="tag_info.source">{{tag_info.text}}</router-link>
  </div>
</template>

<script>
export default {
  props: {
    tag_info: Object,
  },
};
</script>

<style>
#tag {
  font-size: 30px;
  text-align: center;
  color: white;
}
#tag:hover {
  color: rgb(0, 0, 0);
}
</style>