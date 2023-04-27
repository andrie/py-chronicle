py-chronicle
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

\*\* Work in progress \*\*

The purpose of this experimental package is to expose functionality to
make it easy to read, filter and manipulate chronicle parquet files.

## Install

The package is not yet available on PyPi.

``` sh
#| include: False
pip install py_chronicle
```

You can install from github:

``` sh
pip install git+https://github.com/andrie/py-chronicle
```

## How to use

### Working with metrics

Some examples.

``` python
read_chronicle("./data/v1/metrics").head()
```

<div><style>
.dataframe > thead > tr > th,
.dataframe > tbody > tr > td {
  text-align: right;
}
</style>
<small>shape: (5, 13)</small><table border="1" class="dataframe"><thead><tr><th>service</th><th>host</th><th>os</th><th>attributes</th><th>name</th><th>description</th><th>unit</th><th>type</th><th>timestamp</th><th>value_float</th><th>value_int</th><th>value_uint</th><th>value_column</th></tr><tr><td>str</td><td>str</td><td>str</td><td>list[struct[2]]</td><td>str</td><td>str</td><td>str</td><td>str</td><td>datetime[ms]</td><td>f64</td><td>i64</td><td>u64</td><td>str</td></tr></thead><tbody><tr><td>&quot;workbench-metr…</td><td>&quot;rstudio-workbe…</td><td>&quot;linux&quot;</td><td>[{&quot;host&quot;,&quot;rstudio-workbench-6b9658c77f-mn8hj&quot;}]</td><td>&quot;rstudio_system…</td><td>&quot;Graphite metri…</td><td>&quot;&quot;</td><td>&quot;gauge&quot;</td><td>2023-04-03 16:02:20.574</td><td>3.0074e9</td><td>0</td><td>0</td><td>&quot;value_float&quot;</td></tr><tr><td>&quot;workbench-metr…</td><td>&quot;rstudio-workbe…</td><td>&quot;linux&quot;</td><td>[{&quot;host&quot;,&quot;rstudio-workbench-6b9658c77f-mn8hj&quot;}]</td><td>&quot;rstudio_system…</td><td>&quot;Graphite metri…</td><td>&quot;&quot;</td><td>&quot;gauge&quot;</td><td>2023-04-03 16:02:20.574</td><td>3.2212e9</td><td>0</td><td>0</td><td>&quot;value_float&quot;</td></tr><tr><td>&quot;workbench-metr…</td><td>&quot;rstudio-workbe…</td><td>&quot;linux&quot;</td><td>[{&quot;host&quot;,&quot;rstudio-workbench-6b9658c77f-mn8hj&quot;}]</td><td>&quot;rstudio_system…</td><td>&quot;Graphite metri…</td><td>&quot;&quot;</td><td>&quot;gauge&quot;</td><td>2023-04-03 16:02:20.574</td><td>2.13864448e8</td><td>0</td><td>0</td><td>&quot;value_float&quot;</td></tr><tr><td>&quot;connect-metric…</td><td>&quot;rstudio-connec…</td><td>&quot;linux&quot;</td><td>[{&quot;host&quot;,&quot;rstudio-connect-68785f94cc-qzvrm&quot;}]</td><td>&quot;rsconnect_syst…</td><td>&quot;Graphite metri…</td><td>&quot;&quot;</td><td>&quot;gauge&quot;</td><td>2023-04-03 16:24:29.980</td><td>5.7377e9</td><td>0</td><td>0</td><td>&quot;value_float&quot;</td></tr><tr><td>&quot;connect-metric…</td><td>&quot;rstudio-connec…</td><td>&quot;linux&quot;</td><td>[{&quot;host&quot;,&quot;rstudio-connect-68785f94cc-qzvrm&quot;}]</td><td>&quot;rsconnect_syst…</td><td>&quot;Graphite metri…</td><td>&quot;&quot;</td><td>&quot;gauge&quot;</td><td>2023-04-03 16:24:29.980</td><td>7.04741376e8</td><td>0</td><td>0</td><td>&quot;value_float&quot;</td></tr></tbody></table></div>

``` python
read_chronicle("./data/v1/metrics/").metrics.describe()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>service</th>
      <th>name</th>
      <th>description</th>
      <th>value_column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>connect-metrics</td>
      <td>rsconnect_system_memory_available</td>
      <td>[Graphite metric rsconnect_system_memory_avail...</td>
      <td>[value_float]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>connect-metrics</td>
      <td>rsconnect_system_memory_total</td>
      <td>[Graphite metric rsconnect_system_memory_total]</td>
      <td>[value_float]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>connect-metrics</td>
      <td>rsconnect_system_memory_used</td>
      <td>[Graphite metric rsconnect_system_memory_used]</td>
      <td>[value_float]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>workbench-metrics</td>
      <td>rstudio_system_memory_available</td>
      <td>[Graphite metric rstudio_system_memory_available]</td>
      <td>[value_float]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>workbench-metrics</td>
      <td>rstudio_system_memory_total</td>
      <td>[Graphite metric rstudio_system_memory_total]</td>
      <td>[value_float]</td>
    </tr>
    <tr>
      <th>5</th>
      <td>workbench-metrics</td>
      <td>rstudio_system_memory_used</td>
      <td>[Graphite metric rstudio_system_memory_used]</td>
      <td>[value_float]</td>
    </tr>
  </tbody>
</table>
</div>

``` python
read_chronicle("./data/v1/metrics/").metrics.filter("rsconnect_system_memory_used", "memory").head()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>host</th>
      <th>timestamp</th>
      <th>memory</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>rstudio-connect-68785f94cc-qzvrm</td>
      <td>2023-04-03 16:00:29.980</td>
      <td>1.170264e+09</td>
    </tr>
    <tr>
      <th>1</th>
      <td>rstudio-connect-68785f94cc-qzvrm</td>
      <td>2023-04-03 16:01:29.980</td>
      <td>1.187889e+09</td>
    </tr>
    <tr>
      <th>2</th>
      <td>rstudio-connect-68785f94cc-qzvrm</td>
      <td>2023-04-03 16:02:29.980</td>
      <td>1.188659e+09</td>
    </tr>
    <tr>
      <th>3</th>
      <td>rstudio-connect-68785f94cc-qzvrm</td>
      <td>2023-04-03 16:03:29.980</td>
      <td>1.252348e+09</td>
    </tr>
    <tr>
      <th>4</th>
      <td>rstudio-connect-68785f94cc-qzvrm</td>
      <td>2023-04-03 16:04:29.980</td>
      <td>1.259856e+09</td>
    </tr>
  </tbody>
</table>
</div>

``` python
read_chronicle("./data/v1/metrics/").metrics.plot("rsconnect_system_memory_used", "memory")
```

    Unable to display output for mime type(s): application/vnd.plotly.v1+json

### Working with logs

``` python
read_chronicle("./data/v1/logs").head()
```

<div><style>
.dataframe > thead > tr > th,
.dataframe > tbody > tr > td {
  text-align: right;
}
</style>
<small>shape: (5, 6)</small><table border="1" class="dataframe"><thead><tr><th>service</th><th>host</th><th>os</th><th>attributes</th><th>body</th><th>timestamp</th></tr><tr><td>str</td><td>str</td><td>str</td><td>list[struct[2]]</td><td>str</td><td>datetime[ms]</td></tr></thead><tbody><tr><td>&quot;workbench&quot;</td><td>&quot;rstudio-workbe…</td><td>&quot;linux&quot;</td><td>[{&quot;data&quot;,&quot;120&quot;}, {&quot;pid&quot;,&quot;2.36E+02&quot;}, … {&quot;type&quot;,&quot;session_suspend&quot;}]</td><td>&quot;{&quot;pid&quot;:236,&quot;us…</td><td>2023-04-03 18:01:26.665</td></tr><tr><td>&quot;workbench&quot;</td><td>&quot;rstudio-workbe…</td><td>&quot;linux&quot;</td><td>[{&quot;data&quot;,&quot;&quot;}, {&quot;pid&quot;,&quot;2.36E+02&quot;}, … {&quot;type&quot;,&quot;session_exit&quot;}]</td><td>&quot;{&quot;pid&quot;:236,&quot;us…</td><td>2023-04-03 18:01:26.761</td></tr><tr><td>&quot;connect&quot;</td><td>&quot;rstudio-connec…</td><td>&quot;linux&quot;</td><td>[{&quot;user_role&quot;,&quot;publisher&quot;}, {&quot;user_guid&quot;,&quot;085ba4be-01b5-478b-877c-321368924c89&quot;}, … {&quot;type&quot;,&quot;audit&quot;}]</td><td>&quot;{&quot;action&quot;:&quot;add…</td><td>2023-04-03 19:30:35.698</td></tr><tr><td>&quot;connect&quot;</td><td>&quot;rstudio-connec…</td><td>&quot;linux&quot;</td><td>[{&quot;log.file.name&quot;,&quot;audit.json&quot;}, {&quot;actor_description&quot;,&quot;Auth Provider&quot;}, … {&quot;entry_id&quot;,&quot;3.032E+03&quot;}]</td><td>&quot;{&quot;action&quot;:&quot;add…</td><td>2023-04-03 19:30:35.698</td></tr><tr><td>&quot;connect&quot;</td><td>&quot;rstudio-connec…</td><td>&quot;linux&quot;</td><td>[{&quot;action&quot;,&quot;add_group_member&quot;}, {&quot;actor_id&quot;,&quot;0E+00&quot;}, … {&quot;log.file.name&quot;,&quot;audit.json&quot;}]</td><td>&quot;{&quot;action&quot;:&quot;add…</td><td>2023-04-03 19:30:35.698</td></tr></tbody></table></div>

``` python
read_chronicle("./data/v1/logs").logs.filter_type("username").head()
```

<div><style>
.dataframe > thead > tr > th,
.dataframe > tbody > tr > td {
  text-align: right;
}
</style>
<small>shape: (5, 6)</small><table border="1" class="dataframe"><thead><tr><th>service</th><th>host</th><th>timestamp</th><th>.username</th><th>.type</th><th>body</th></tr><tr><td>str</td><td>str</td><td>datetime[ms]</td><td>str</td><td>str</td><td>str</td></tr></thead><tbody><tr><td>&quot;workbench&quot;</td><td>&quot;rstudio-workbe…</td><td>2023-04-03 18:01:26.761</td><td>&quot;james&quot;</td><td>&quot;session_exit&quot;</td><td>&quot;{&quot;pid&quot;:236,&quot;us…</td></tr><tr><td>&quot;workbench&quot;</td><td>&quot;rstudio-workbe…</td><td>2023-04-07 03:46:57.960</td><td>&quot;james&quot;</td><td>&quot;auth_login&quot;</td><td>&quot;{&quot;pid&quot;:1059,&quot;u…</td></tr><tr><td>&quot;workbench&quot;</td><td>&quot;rstudio-workbe…</td><td>2023-04-07 03:51:15.161</td><td>&quot;james&quot;</td><td>&quot;session_start&quot;</td><td>&quot;{&quot;pid&quot;:236,&quot;us…</td></tr><tr><td>&quot;workbench&quot;</td><td>&quot;rstudio-workbe…</td><td>2023-04-07 04:19:18.561</td><td>&quot;james&quot;</td><td>&quot;session_exit&quot;</td><td>&quot;{&quot;pid&quot;:236,&quot;us…</td></tr><tr><td>&quot;workbench&quot;</td><td>&quot;rstudio-workbe…</td><td>2023-04-07 04:19:19.764</td><td>&quot;james&quot;</td><td>&quot;session_start&quot;</td><td>&quot;{&quot;pid&quot;:883,&quot;us…</td></tr></tbody></table></div>

### 
