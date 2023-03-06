# Tools

## Coverter

```{note}

Test!

- adapted from [Youtube](https://www.youtube.com/watch?v=Muy1gCsK7vA)

```

<div class="container">
<form id="calcTemp" onsubmit="calculateTemp(); return false">
<label for="temp">Enter the temperature to convert</label>
<br>
<input type="number" name="temp" id="temp" value="0">
<select name="temp_diff" id="temp_diff">
<option value="cel">&#176;Celsius</option>
<option value="fah">&#176;Fahrenheit</option>
</select>
<br>
<input type="submit" name="temp" id="submit">
<br>
<span id="result"></span>
</form>
</div>

<script src="../_static/assets/T-converter.js"></script>
    