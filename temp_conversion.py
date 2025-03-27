<html>
    <head>
        <title>javascript </title>
            <script>
function celsiusToFahrenheit(celsius) {
    let fahrenheit = (celsius * 9/5) + 32;
    return fahrenheit;
}

let celsius = prompt("Enter temperature in Celsius: ");
let fahrenheit = celsiusToFahrenheit(Number(celsius));
console.log(celsius + "°C is equal to " + fahrenheit + "°F");
</script>
       
    </head>
</html>
