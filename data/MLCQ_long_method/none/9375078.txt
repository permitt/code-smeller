        private PublishingBodySubscriber() {
            completionCF = new MinimalFuture<>();
            completionCF.whenComplete(
                    (r,t) -> subscribedCF.thenAccept( s -> complete(s, t)));
        }