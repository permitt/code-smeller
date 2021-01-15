        public Image createImageFromFile(final String file, final double width, final double height) {
            final long image = nativeCreateNSImageFromFileContents(file);
            nativeSetNSImageSize(image, width, height);
            return createImage(image, width, height);
        }