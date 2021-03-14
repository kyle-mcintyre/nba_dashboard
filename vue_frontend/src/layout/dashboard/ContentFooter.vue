<template>
  <footer class="footer">
    <div class="container-fluid">
      <ul class="nav">
        <li class="nav-item">
          <a class="nav-link" @click="informationClicked">
            About
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href = "mailto: kjmc0707@gmail.com">
            Contact
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href = "">
            Code
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="http://www.creative-tim.com/license">
            License
          </a>
        </li>
      </ul>
    </div>
  </footer>
</template>
<script>
  export default {
    data() {
      return {
      }
    }, 
    methods: {
      informationClicked(){
        this.$info({
          title: 'NBA Dashboard Info',
          // JSX support
          content: (
            <div>
              <p style="color:black">
                The inspiration behind this project is to view a player's trends throughout the season.
                You can search for any active player in the NBA right now and view their season from a holistic view.
              </p>
              <p style="color:black"><b>Author:</b> Kyle McIntyre</p>
              <p style="color:black"><b>Email:</b> kjmc0707@gmail.com</p>
            </div>
          ),
        });
      }
    }
  };
</script>

<style scoped>
#info{
  color: black;
}
</style>
