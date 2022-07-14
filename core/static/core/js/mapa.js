var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 43.5293101, lng: -5.6773233},
    zoom: 13
  });
}
<script async defer
src="https://maps.googleapis.com/maps/api/js?key=AIzaSyA3AA9BFKAu2oBDjupB6Dj1R1qdEEfEJ2w&callback=initMap">
</script>