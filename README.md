# P111 Loader Plugin

## Use Case
Navigation data in OGP P111 format can be used in mapping. The files, however, are generally very large, so only a subset needs to be plotted. Typically, these are the source locations. This plugin reads a P111 file and generates a _LineString_ that represents the line. 

## Status
Theoretical at this stage

## Future Developments
It is also possible to create a _Point_ layer with each source location indexed individually. This can be used for assigning QC metrics to the source locations  directly. A GUI might allow QC values over specific index ranges to be set directly, but this might be better done as a separate plugin.

