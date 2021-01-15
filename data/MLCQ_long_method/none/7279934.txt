                    public ImageArguments crop(CropRegion value) {
                        if (value != null) {
                            startArgument("crop");
                            _queryBuilder.append(value.toString());
                        }
                        return this;
                    }