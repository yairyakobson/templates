import AWS from "aws-sdk";

AWS.config.update({
  accessKeyId: process.env.AWS_ACCESS_KEY_ID || "",
  secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY || "",
  region: process.env.AWS_REGION || "",
});

const s3 = new AWS.S3();

interface UploadResponse {
  public_id: string;
  url: string;
}

interface File {
  name: string;
  buffer: Buffer;
  mimeType: string;
}

export const upload_file = (file: File, folder: string): Promise<UploadResponse> => {
  return new Promise((resolve, reject) => {
    const params: AWS.S3.PutObjectRequest = {
      Bucket: process.env.BUCKET || "",
      Key: `${folder}/${Date.now()}_${file.name}`,
      Body: file.buffer,
      ContentType: file.mimeType,
      ContentDisposition: "inline", // Ensure the image is displayed in the browser
    };

    s3.upload(params, (err, data) => {
      if (err) {
        return reject(err);
      }
      resolve({
        public_id: params.Key,
        url: data.Location,
      });
    });
  });
};

export const delete_file = async (file: string): Promise<boolean> => {
  const params: AWS.S3.DeleteObjectRequest = {
    Bucket: process.env.BUCKET || "",
    Key: file,
  };

  try {
    await s3.deleteObject(params).promise();
    return true;
  } catch (error) {
    console.error("Error deleting file:", error);
    throw new Error("An error occurred");
  }
};