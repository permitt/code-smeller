	static class JetS3tV2 extends WalkEncryption {

		static final String VERSION = "2"; //$NON-NLS-1$

		static final String ALGORITHM = "PBEWithMD5AndDES"; //$NON-NLS-1$

		static final int ITERATIONS = 5000;

		static final int KEY_SIZE = 32;

		static final byte[] SALT = { //
				(byte) 0xA4, (byte) 0x0B, (byte) 0xC8, (byte) 0x34, //
				(byte) 0xD6, (byte) 0x95, (byte) 0xF3, (byte) 0x13 //
		};

		// Size 16, see com.sun.crypto.provider.AESConstants.AES_BLOCK_SIZE
		static final byte[] ZERO_AES_IV = new byte[16];

		private static final String CRYPTO_VER = VERSION;

		private final String cryptoAlg;

		private final SecretKey secretKey;

		private final AlgorithmParameterSpec paramSpec;

		JetS3tV2(final String algo, final String key)
				throws GeneralSecurityException {
			cryptoAlg = algo;

			// Verify if cipher is present.
			Cipher cipher = InsecureCipherFactory.create(cryptoAlg);

			// Standard names are not case-sensitive.
			// http://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html
			String cryptoName = cryptoAlg.toUpperCase(Locale.ROOT);

			if (!cryptoName.startsWith("PBE")) //$NON-NLS-1$
				throw new GeneralSecurityException(JGitText.get().encryptionOnlyPBE);

			PBEKeySpec keySpec = new PBEKeySpec(key.toCharArray(), SALT, ITERATIONS, KEY_SIZE);
			secretKey = SecretKeyFactory.getInstance(algo).generateSecret(keySpec);

			// Detect algorithms which require initialization vector.
			boolean useIV = cryptoName.contains("AES"); //$NON-NLS-1$

			// PBEParameterSpec algorithm parameters are supported from Java 8.
			if (useIV) {
				// Support IV where possible:
				// * since JCE provider uses random IV for PBE/AES
				// * and there is no place to store dynamic IV in JetS3t V2
				// * we use static IV, and tolerate increased security risk
				// TODO back port this change to JetS3t V2
				// See:
				// https://bitbucket.org/jmurty/jets3t/raw/156c00eb160598c2e9937fd6873f00d3190e28ca/src/org/jets3t/service/security/EncryptionUtil.java
				// http://cr.openjdk.java.net/~mullan/webrevs/ascarpin/webrev.00/raw_files/new/src/share/classes/com/sun/crypto/provider/PBES2Core.java
				IvParameterSpec paramIV = new IvParameterSpec(ZERO_AES_IV);
				paramSpec = new PBEParameterSpec(SALT, ITERATIONS, paramIV);
			} else {
				// Strict legacy JetS3t V2 compatibility, with no IV support.
				paramSpec = new PBEParameterSpec(SALT, ITERATIONS);
			}

			// Verify if cipher + key are allowed by policy.
			cipher.init(Cipher.ENCRYPT_MODE, secretKey, paramSpec);
			cipher.doFinal();
		}

		@Override
		void request(HttpURLConnection u, String prefix) {
			u.setRequestProperty(prefix + JETS3T_CRYPTO_VER, CRYPTO_VER);
			u.setRequestProperty(prefix + JETS3T_CRYPTO_ALG, cryptoAlg);
		}

		@Override
		void validate(HttpURLConnection u, String prefix)
				throws IOException {
			validateImpl(u, prefix, CRYPTO_VER, cryptoAlg);
		}

		@Override
		OutputStream encrypt(OutputStream os) throws IOException {
			try {
				final Cipher cipher = InsecureCipherFactory.create(cryptoAlg);
				cipher.init(Cipher.ENCRYPT_MODE, secretKey, paramSpec);
				return new CipherOutputStream(os, cipher);
			} catch (GeneralSecurityException e) {
				throw error(e);
			}
		}

		@Override
		InputStream decrypt(InputStream in) throws IOException {
			try {
				final Cipher cipher = InsecureCipherFactory.create(cryptoAlg);
				cipher.init(Cipher.DECRYPT_MODE, secretKey, paramSpec);
				return new CipherInputStream(in, cipher);
			} catch (GeneralSecurityException e) {
				throw error(e);
			}
		}
	}