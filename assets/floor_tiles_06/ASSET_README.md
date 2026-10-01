# Floor Tiles 06 — source asset

Extracted from the user-supplied `floor_tiles_06_4k.blend.zip`. The Blender file and the 4K colour/roughness textures are stored intact. The 4K OpenEXR normal map and 16-bit PNG displacement map are stored as byte-for-byte source parts because the GitHub upload endpoint accepts at most 16 MiB per file. From this folder run `python3 restore_source_maps.py` to reassemble them; the script verifies exact byte sizes and SHA-256 hashes before writing either map.

`source_manifest.json` records the uploaded archive hash, the individual source hashes, and the original license status. The supplied ZIP contained no license statement, so check the source license before redistribution beyond this asset library. Keep the source maps unchanged when deriving smaller web-ready copies.
